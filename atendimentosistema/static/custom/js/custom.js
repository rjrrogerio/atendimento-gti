$(function () {
  /*
  $('#tipodefuncionario').on('change', function (e) {
    var optionSelected = $("option:selected", this);
    var valueSelected = this.value;
    console.log(valueSelected)
    if (valueSelected == 3) {
      $(".licenca").hide();

    } else {
      $(".licenca").show();
    }
  });

  $('#tipodefuncionario').on('change', function (e) {
    var optionSelected = $("option:selected", this);
    var valueSelected = this.value;
    console.log(valueSelected)
    if (valueSelected == 1) {
      $(".datacontrato").hide();

    } else {
      $(".datacontrato").show();
    }
  });*/

  var maxField = 10; //Input fields increment limitation
  var addButton = $('.add_button'); //Add button selector
  var wrapper = $('.field_wrapper'); //Input field wrapper
  var x = 1; //Initial field counter is 1

  
  //Once add button is clicked
  $(addButton).click(function () {
    //Check maximum number of input fields
    if (x < maxField) {
      var fieldHTML = '<div class="row"> <div class="col-3 m-1"> <input class="form-control " type="text" name="field_nome['+x+']" value="" placeholder="Nome completo" /> </div> <div class="col-2 m-1"> <input class="form-control " type="text" name="field_email['+x+']" value="" placeholder="nome@sescsp.org.br" /> </div> <div class="col-1 m-1"> <input class="form-control " type="text" name="field_uo['+x+']" value="" placeholder="UO" /> </div> <div class="col-2 m-1"> <select class="form-control" name="field_tipo['+x+']" aria-label=".form-select-lg example" id="tipodefuncionario"> <option selected value="funcionario">Funcionário</option> <option value="estagiario">Estagiário</option><option value="pj">PJ</option> <option value="temporario">Temporário</option> </select> </div> <div class="col-1 m-1"> <select class="form-control" name="field_licenca['+x+']" aria-label=".form-select-sm example" id="tipodelicenca"> <option selected value="lica1">LIC-A1</option> <option value="lica3" name="lica3">LIC-A3</option> </select> </div> <div class="col-2 m-1 datacontrato"> <input class="form-control" type="date" name="field_datacontrato['+x+']" placeholder="Data do contrato"> </div> </div>'; //New input field html 
      x++; //Increment field counter
      $(wrapper).append(fieldHTML); //Add field html
      document.getElementById('countField').value = x
    }
  });

});


