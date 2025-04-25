public class ListaDupla{
    private No inicio;
    private No fim;

    public listaVazia(){
        this.inicio = null;
        this.fim = null;
    }


    public boolean Vazio(){
        return ((this.inicio == Null) && (this.fim ==null));
    }

    public boolean insereprimeirono (double valor){
        if (!listaVazia()) return false;

        No aux = new this.No(valor);
        this.inicio=aux;
        this.fim=aux;
        return true
    }
   public String imprimir(){
        if (listaVazia()) return "lsita vazia";

        No aux = this.inicio;
        String temp = ""+ aux.getValor()+" ";
        while(aux.getProx() != null){
            aux = aux.getProx();
            temp = temp + aux.getValor()+" ";
        }
        return temp;
        
    public boolean inserefinallista (double valor){
        
        
    }


   }





}