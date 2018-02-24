public class ValorObservable extends Observable { 
	private int nValor = 0; 

	public ValorObservable(int nValor,int nInferior,int nSuperior ) { 
		this.nValor = nValor; 
	}
	public void setValor(int nValor) { 
		this.nValor = nValor; 
		setChanged(); 
		notifyObservers();
	} 
	public int getValor() { 
		return (nValor); 
	} 
}
