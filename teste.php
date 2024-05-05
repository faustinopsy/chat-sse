<?php
class Carro {
    public String $marca;
    public String $modelo;
    public String $ano;

    public function __construct($marca, $modelo, $ano) {
        $this->marca = $marca;
        $this->modelo = $modelo;
        $this->ano = $ano;
    }

    public function exibirInformacoes() {
        return "Marca: $this->marca, Modelo: $this->modelo, Ano: $this->ano \n";
    }
}
echo "Uso da memória antes da instância: " . memory_get_usage() . " bytes\n";

$meuCarro = new Carro("Toyota", "Corolla", 2020);
echo "Uso da memória após a instância: " . memory_get_usage() . " bytes\n";
echo $meuCarro->exibirInformacoes();
echo "Uso da memória após a instância: " . memory_get_usage() . " bytes\n";