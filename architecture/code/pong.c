int main (int argc, char* argv[]) {
	init_game(); // Game initialization

	while (1) {  // Game loop
		capture_events(); // Capture events
		if (exitKeyPressed()) break; // Exit
		move_paddles(); // Update paddles
		move_ball();	// update ball
		collision_detection();
		if (ballReachedBorder(LEFT_PLAYER)) {
			score(RIGHT_PLAYER);
			reset_ball();
		}
		if (ballReachedBorder(RIGHT_PLAYER)) {
			score(LEFT_PLAYER);
			reset_ball();
		}
		render();
	}
}
