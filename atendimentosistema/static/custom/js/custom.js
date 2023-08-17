$(function () {

  $("body").on("change", '#tipodefuncionario', function (e) {
    var valueSelected = this.value;
    var nameField = this.name;
    var numberField = nameField.replace(/[^0-9]/g, '');

    if (valueSelected == "funcionario") {
      document.getElementById('datacontrato[' + numberField + ']').style.display = "none";
    } else {
      document.getElementById('datacontrato[' + numberField + ']').style.display = "block";
    }
  })

  var maxField = 20; //Input fields increment limitation
  var addButton = $('.add_button');
  var removeButton = $('.remove_button');
  var wrapper = $('.field_wrapper');
  var x = 1; //Initial field counter is 1
  
  //when add button is clicked
  $(addButton).click(function () {
    if (x < maxField) {
      var fieldHTML = '<div class="row line' + x + '" > <div class="col-3 m-1"> <input class="form-control " type="text" name="field_nome[' + x + ']" value="" placeholder="Nome completo" required="required"/> </div> <div class="col-2 m-1"> <input class="form-control " type="text" name="field_email[' + x + ']" value="" placeholder="nome.sobrenome" required="required"/> </div> <div class="col-1 m-1"> <input class="form-control " type="text" name="field_uo[' + x + ']" value="" placeholder="UO" required="required"/> </div> <div class="col-2 m-1"> <select class="form-control" name="field_tipo[' + x + ']" aria-label=".form-select-lg example" id="tipodefuncionario"> <option selected value="funcionario">Funcionário</option> <option value="estagiario">Estagiário</option><option value="pj">PJ</option> <option value="temporario">Temporário</option> </select> </div> <div class="col-1 m-1"> <select class="form-control" name="field_licenca[' + x + ']" aria-label=".form-select-sm example" id="tipodelicenca"> <option selected value="lica1">LIC-A1</option> <option value="lica3" name="lica3">LIC-A3</option> </select> </div> <div class="col-2 m-1" id="datacontrato[' + x + ']" style="display: none"> <input class="form-control" id="datacontrato" type="date" name="field_datacontrato[' + x + ']" placeholder="Data do contrato"> </div> </div>';
      $(wrapper).append(fieldHTML);
      x++;
      document.getElementById('countField').value = x
    }
  });
  $(removeButton).click(function () {
    if (x != 1){
      x--;
    }
    var elems = document.querySelectorAll('.line' + x);    
    document.getElementById('countField').value = x
    elems.forEach(function (element) {
      element.parentNode.removeChild(element);
    });
  });
});


