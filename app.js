// Configuration
const CONFIG = {
    SWIPE_THRESHOLD: 100,
    MAX_OFFSET: 200,
    ANIMATION_DURATION: 300, // ms
    FEEDBACK_DELAY: 200 // ms
};

// State Management
const state = {
    cards: [],
    nextCardData: null,
    touchState: {
        startX: 0,
        currentX: 0,
        endX: 0,
        isSwiping: false
    }
};

// DOM Elements
const elements = {
    flashcard: document.getElementById('flashcard'),
    frontContent: document.getElementById('front-content'),
    backContent: document.getElementById('back-content'),
    solutionContent: document.getElementById('solution-content'),
    themeButton: document.getElementById('theme-button')
};

// Card Management
const cardManager = {
    async preCacheNextCard() {
        try {
            if (state.cards.length === 0) {
                const response = await fetch('card-list.txt');
                state.cards = (await response.text()).trim().split('\n');
            }
            const randomCard = state.cards[Math.floor(Math.random() * state.cards.length)];

            const [front, back, solution, meta] = await Promise.all([
                fetch(`cards/${randomCard}/front.md`).then(r => r.text()),
                fetch(`cards/${randomCard}/back.md`).then(r => r.text()),
                fetch(`cards/${randomCard}/solution.py`).then(r => r.text()),
                fetch(`cards/${randomCard}/meta.json`).then(r => r.json())
            ]);

            state.nextCardData = { front, back, solution, meta };
        } catch (error) {
            console.error('Error pre-caching next card:', error);
        }
    },

    async loadCard() {
        try {
            elements.frontContent.innerHTML = `
                <div class="card-title">${state.nextCardData.meta.name}</div>
                ${marked.parse(state.nextCardData.front)}
            `;
            elements.backContent.innerHTML = `
                <div class="card-title">${state.nextCardData.meta.name}</div>
                ${marked.parse(state.nextCardData.back)}
            `;
            elements.solutionContent.innerHTML =
                `<h2>Solution</h2><pre><code class="language-python">${state.nextCardData.solution}</code></pre>`;

            // Generate ChatGPT explanation link
            const prompt =
                'Explain the problem "' + state.nextCardData.meta.name + '" technical coding interview question in detail. ' +
                'Break down the solution approach and explain how this Python code works:\n\n' +
                '```python\n' +
                state.nextCardData.solution + '\n' +
                '```\n\n' +
                'Provide additional examples and explain any technical terms. ' +
                'Use simple language and include diagrams if helpful.';
            const encodedPrompt = encodeURIComponent(prompt);
            const chatGPTLink = `https://chat.openai.com/?model=gpt-4&q=${encodedPrompt}`;
            document.getElementById('chatgpt-link').href = chatGPTLink;

            hljs.highlightAll();

            state.nextCardData = null;
            this.preCacheNextCard();
        } catch (error) {
            console.error('Error loading card:', error);
        }
    }
};

// UI Interactions
const uiManager = {
    toggleTheme() {
        document.body.classList.toggle('dark-mode');
        elements.themeButton.textContent =
            document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
    },

    flipCard() {
        if (!state.touchState.isSwiping) {
            const front = document.querySelector('.card-front');
            const back = document.querySelector('.card-back');

            elements.flashcard.classList.toggle('flipped');
            elements.flashcard.style.transition = `transform ${CONFIG.ANIMATION_DURATION}ms ease-out`;
            elements.flashcard.style.transform = elements.flashcard.classList.contains('flipped')
                ? 'rotateY(180deg)'
                : '';

            // Handle pointer events
            if (elements.flashcard.classList.contains('flipped')) {
                front.classList.add('no-pointer-events');
                back.classList.remove('no-pointer-events');
            } else {
                back.classList.add('no-pointer-events');
                front.classList.remove('no-pointer-events');
            }
        }
    },

    handleFeedback(isCorrect) {
        elements.flashcard.classList.remove('swipe-left', 'swipe-right', 'flipped');
        elements.flashcard.style.transform = '';
        elements.flashcard.style.transition = 'none';

        const front = document.querySelector('.card-front');
        const back = document.querySelector('.card-back');
        front.classList.remove('no-pointer-events');
        back.classList.remove('no-pointer-events');
        back.classList.add('no-pointer-events');

        cardManager.loadCard();
    }
};

// Touch Handling
const touchManager = {
    handleTouchStart(e) {
        // Skip if touch started in code block
        if (e.target.closest('pre')) return;

        state.touchState = {
            startX: e.touches[0].clientX,
            currentX: 0,
            isSwiping: false
        };
        elements.flashcard.style.transition = 'none';
    },

    handleTouchMove(e) {
        // Skip if touch started in code block
        if (e.target.closest('pre')) return;

        const touchX = e.touches[0].clientX;
        const deltaX = touchX - state.touchState.startX;

        if (Math.abs(deltaX) > 10) {
            state.touchState.isSwiping = true;
            e.preventDefault();

            state.touchState.currentX = deltaX;

            // Preserve flip state during transform
            if (elements.flashcard.classList.contains('flipped')) {
                elements.flashcard.style.transform = `translateX(${deltaX}px) rotateY(180deg)`;
            } else {
                elements.flashcard.style.transform = `translateX(${deltaX}px)`;
            }
        }
    },

    handleTouchEnd(e) {
        // Skip if touch started in code block
        if (e.target.closest('pre')) return;

        if (state.touchState.isSwiping) {
            const isSwipeRight = state.touchState.currentX > 0;
            const passedThreshold = Math.abs(state.touchState.currentX) >= CONFIG.SWIPE_THRESHOLD;

            elements.flashcard.style.transition = `transform ${CONFIG.ANIMATION_DURATION}ms ease-out`;

            if (passedThreshold) {
                const screenWidth = window.innerWidth;
                const endPosition = isSwipeRight ? screenWidth : -screenWidth;

                if (elements.flashcard.classList.contains('flipped')) {
                    elements.flashcard.style.transform = `translateX(${endPosition}px) rotateY(180deg)`;
                } else {
                    elements.flashcard.style.transform = `translateX(${endPosition}px)`;
                }
                setTimeout(() => uiManager.handleFeedback(isSwipeRight), CONFIG.FEEDBACK_DELAY);
            } else {
                // Return to center while preserving flip state
                if (elements.flashcard.classList.contains('flipped')) {
                    elements.flashcard.style.transform = 'translateX(0) rotateY(180deg)';
                } else {
                    elements.flashcard.style.transform = 'translateX(0)';
                }
            }
        }
    }
};

// Event Listeners
function initializeEventListeners() {
    // Touch events
    elements.flashcard.addEventListener('touchstart', touchManager.handleTouchStart);
    elements.flashcard.addEventListener('touchmove', touchManager.handleTouchMove);
    elements.flashcard.addEventListener('touchend', touchManager.handleTouchEnd);

    // Service Worker Registration
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('ServiceWorker registration successful');
                })
                .catch(err => {
                    console.log('ServiceWorker registration failed: ', err);
                });
        });
    }
}

// Initialize Application
function initializeApp() {
    // Set initial theme
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark-mode');
        elements.themeButton.textContent = '☀️';
    }

    initializeEventListeners();

    // Load first card
    cardManager.preCacheNextCard().then(() => cardManager.loadCard());
}

// Start the application
initializeApp();

// Expose necessary functions for HTML event handlers
window.toggleTheme = uiManager.toggleTheme;
window.flipCard = uiManager.flipCard;
window.handleFeedback = uiManager.handleFeedback;
