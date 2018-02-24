while(running) {
	checkUserInput();
	runAI();
	moveEnemies();
	resolveCollisions();
	drawGraphics(); //Render loop
	playSound();
}
