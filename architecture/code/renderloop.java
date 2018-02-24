while (true) {
	// Update camera, usually according to a 
	// predefined path
	updateCamera();

	// Update position, orientation and rest
	// of the state of the entities in the game
	updateSceneEntitites();

	// Render a frame in a buffer
	renderScene();

	// Interchage the buffer to visualize the image
	swapBuffers();
}
