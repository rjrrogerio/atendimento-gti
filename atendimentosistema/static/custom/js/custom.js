$(function () {
  
  $("body").on("change",'#tipodefuncionario', function (e) {
    var valueSelected = this.value;
    var nameField = this.name;
    var numberField = nameField.replace(/[^0-9]/g, '');
    
    if (valueSelected == "funcionario") {
      console.log(numberField)
      document.getElementById('datacontrato['+numberField+']').style.display = "none";
    } else {
      console.log(numberField)  
      document.getElementById('datacontrato['+numberField+']').style.display = "block";
    }
  })

  var maxField = 20; //Input fields increment limitation
  var addButton = $('.add_button'); //Add button selector
  var wrapper = $('.field_wrapper'); //Input field wrapper
  var x = 1; //Initial field counter is 1

  
  //Once add button is clicked
  $(addButton).click(function () {
    //Check maximum number of input fields
    if (x < maxField) {
      var fieldHTML = '<div class="row"> <div class="col-3 m-1"> <input class="form-control " type="text" name="field_nome['+x+']" value="" placeholder="Nome completo" /> </div> <div class="col-2 m-1"> <input class="form-control " type="text" name="field_email['+x+']" value="" placeholder="nome@sescsp.org.br" /> </div> <div class="col-1 m-1"> <input class="form-control " type="text" name="field_uo['+x+']" value="" placeholder="UO" /> </div> <div class="col-2 m-1"> <select class="form-control" name="field_tipo['+x+']" aria-label=".form-select-lg example" id="tipodefuncionario"> <option selected value="funcionario">Funcionário</option> <option value="estagiario">Estagiário</option><option value="pj">PJ</option> <option value="temporario">Temporário</option> </select> </div> <div class="col-1 m-1"> <select class="form-control" name="field_licenca['+x+']" aria-label=".form-select-sm example" id="tipodelicenca"> <option selected value="lica1">LIC-A1</option> <option value="lica3" name="lica3">LIC-A3</option> </select> </div> <div class="col-2 m-1" id="datacontrato['+x+']" style="display: none"> <input class="form-control" id="datacontrato" type="date" name="field_datacontrato['+x+']" placeholder="Data do contrato"> </div> </div>'; //New input field html 
      x++; //Increment field counter
      $(wrapper).append(fieldHTML); //Add field html
      document.getElementById('countField').value = x
    }
  });

});


