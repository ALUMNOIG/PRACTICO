# HTML5 Jigsaw Puzzle Game

A web-based jigsaw puzzle game created with HTML, CSS, and JavaScript. Users can provide an image URL, and the game slices it into a grid of pieces to be solved.

## Features

*   **Dynamic Image Loading:** Load puzzles from any publicly accessible image URL.
*   **Grid-Based Puzzles:** Image is sliced into a grid (e.g., 4x4 by default).
*   **Interactive Gameplay:**
    *   Drag and drop pieces from a selection area to the puzzle board.
    *   One hint piece is correctly placed on the board to start.
*   **Difficulty Levels:** Choose from different grid sizes:
    *   Easy (3x3)
    *   Medium (4x4)
    *   Hard (5x5)
    *   Very Hard (6x6)
*   **Game Controls:**
    *   **"Start Game" Button:** Initiates the puzzle with the provided image URL and selected difficulty.
    *   **"Done" Button:** Validates the player's solution. Correctly placed pieces stay; incorrect ones are highlighted and returned to the selection area.
    *   **"Give Up" Button:** Ends the current game and displays the complete solution.
*   **Countdown Timer:** A 5-minute timer adds a challenge to the game. Time's up results in a game over.
*   **Responsive (Basic):** The puzzle board attempts to fit its container. Pieces in the selection area will scroll if they overflow.
*   **Touch Support:** Playable on smartphones and tablets using touch gestures to drag and drop pieces.

## How to Play

1.  **Open `index.html`:** Since this is a single-file HTML application, simply open the `index.html` file in a modern web browser (e.g., Chrome, Firefox, Edge, Safari).
2.  **Select Difficulty:** Choose your desired grid size from the dropdown menu (e.g., 3x3, 4x4, 5x5, 6x6).
3.  **Enter Image URL:** Paste the URL of an image you want to use for the puzzle into the input field.
    *   Ensure the image URL is publicly accessible and allows cross-origin requests (CORS). If you have trouble with some URLs, try images from sources known to support CORS (e.g., Wikimedia Commons, Imgur direct links).
4.  **Start Game:** Click the "Start Game" button.
5.  **Solve the Puzzle:**
    *   The puzzle board (`frame1`, typically the larger upper frame) will show an empty grid with one piece correctly placed as a hint.
    *   The remaining pieces will be shuffled and displayed in the selection area (`frame2`, typically the lower frame).
    *   Drag pieces from `frame2` and drop them onto the empty slots in `frame1`.
6.  **Check Solution:** Once you believe all pieces are correctly placed, click the "Done" button.
    *   If correct, you'll receive a success message!
    *   If incorrect, any misplaced pieces will be returned to `frame2` for you to try again.
7.  **Timer:** Keep an eye on the 5-minute countdown timer! If it runs out, the game is over.
8.  **Give Up:** If you're stuck or want to see the solution, click the "Give Up" button.

## Technical Details

*   **Frontend:** Pure HTML, CSS, and JavaScript (ES6+).
*   **No Backend:** The game runs entirely in the browser.
*   **Image Slicing:** Uses the HTML `<canvas>` element to load, draw, and slice the source image into pieces.
*   **Drag and Drop:** Native HTML Drag and Drop API (for mouse) and touch event handling (`touchstart`, `touchmove`, `touchend`) for touch devices.
*   **Structure:** All code (HTML, CSS, JS) is contained within the `index.html` file.

## Future Considerations / Potential Enhancements

*   Refinements to touch drag behavior (e.g., animation on snap-back if not dropped on a target).
*   Advanced animations for piece movements and interactions.
*   Saving game progress or high scores (would require backend or local storage).
*   A curated list of default puzzles.
*   Sound effects.
*   More robust error handling for image loading.
