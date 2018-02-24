public class TextoObservador extends Frame implements Observer { 
	private ValorObservable vo = null; 
	
	public TextoObservador( ValorObservable vo ) { 
		this.vo = vo; 
	} 
	public void update(Observable obs, Object obj) { 
		if( obs == vo ) 
			tf.setText(String.valueOf(vo.getValor())); 
	} 
}
