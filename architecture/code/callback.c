void update (unsigned char key, int x, int y) {
	Rearthyear += 0.2;
	Rearthday += 0.2;
	glutPostRedisplay();
}
// More code
int main (int argc, char** argv) {
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
	glutInitWindowSize(640, 480);
	glutCreateWindow("Session #04 - Solar System");
	// Define callbacks
	glutDisplayFunc(display);
	glutReshapeFunc(resize);
	glutKeyboardFunc(update);

	glutMainLoop();
	return 0;
}
