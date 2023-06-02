function carregarDados() {
  // Obtenha o valor selecionado do elemento <select>
  var valorSelecionado = document.getElementById("select-modelo").value;
  
  // Faça a requisição AJAX para o arquivo HTML correspondente ao valor selecionado
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/tabelas/" + valorSelecionado + ".html");
  xhr.onload = function() {
    if (xhr.status === 200) {
      // Atualize o <div> com os dados da tabela obtidos na requisição
      document.getElementById("tabela-de-dados").innerHTML = xhr.responseText;
    }
  };
  xhr.send();
}

// Adicione aqui o código para selecionar automaticamente a opção "rtx4090"
window.addEventListener("load", function() {
  // Verifique se a página atual é a "placasdevideo/index.html"
  if (window.location.pathname === "/placasdevideo/index.html") {
    // Se for, selecione a opção "rtx4090" no elemento <select>
    document.getElementById("select-modelo").value = "RTX 4090";
    // E chame a função carregarDados() para carregar os dados correspondentes
    carregarDados();
  }
});

