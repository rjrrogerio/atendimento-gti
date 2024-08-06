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

  var maxField = 35; //Input fields increment limitation
  var addButton = $('.add_button');
  var changeButton = $('.change_button');
  var disableButton = $('.disable_button');
  var removeButton = $('.remove_button');
  var copyGroupButton = $('.copy_group_button');
  var wrapper = $('.field_wrapper');
  var x = 1; //Initial field counter is 1
  //when add button is clicked
  $(addButton).click(function () {    
    if (x < maxField) {
      var fieldHTML = '<div class="row line'+x+'" > <div class="col-3 m-1"> <input class="form-control " type="text" name="field_nome['+x+']" value="" placeholder="Nome completo" required="required"/> </div> <div class="col-2 m-1" id="id_field_email"> <input class="form-control" type="text" id="field_email" name="field_email['+x+']" value="" placeholder="nome.sobrenome" required="required"/> </div><div class="col-2 m-1"> <select class="form-control" name="field_tipo['+x+']" aria-label=".form-select-lg example" id="tipodefuncionario"> <option selected value="funcionario">Funcionário</option> <option value="estagiario">Estagiário</option><option value="pj">Terceiro</option> <option value="temporario">Temporário</option><option value="aprendiz">Aprendiz</option></select> </div> <div class="col-1 m-1"> <select class="form-control" name="field_licenca['+x+']" aria-label=".form-select-sm example" id="tipodelicenca"> <option selected value="lica1">LIC-A1</option> <option value="lica3" name="lica3">LIC-A3</option> </select> </div> <div class="col-2 m-1" id="datacontrato['+x+']" style="display: none"> <input class="form-control" id="datacontrato" type="date" name="field_data_contrato['+x+']" placeholder="Data do contrato"> </div> </div>';
      
      $(wrapper).append(fieldHTML);
      $('#id_field_uo')
      .clone()
      .attr('id', 'field_uo-'+x)
      .insertAfter($('[id^=id_field_email]:last'));
      const innerDiv = document.getElementById('field_uo-'+x).querySelector('#field_uo')
      //const innerDiv = document.getElementById('field_uo-'+x++)
      innerDiv.setAttribute("name","field_uo["+x+"]")
      x++;   
      document.getElementById('countField').value = x
    }
  });
  $(changeButton).click(function () {    
    if (x < maxField) {
      var fieldHTML = '<div class="row line'+x+'" ><div class="col-4 m-1" id="id_field_email"> <input class="form-control" type="text" id="field_email" name="field_email['+x+']" value="" placeholder="nome.sobrenome" required="required"/> </div><div class="col-2 m-1"> <select class="form-control" name="field_licenca['+x+']" aria-label=".form-select-sm example" id="tipodelicenca"> <option selected value="LIC-A1-SESCSP-SG">LIC-A1</option><option value="LIC-A1-APRENDIZES_SG">LIC-A1 Aprendiz</option><option value="LIC-A1-ESTAGIARIOS_SG">LIC-A1 Estágiário</option><option value="LIC-A1-TEMPORARIOS_SG">LIC-A1 Temporário</option><option value="LIC-A1-TEMPORARIOS_SG_TER">LIC-A1 Terceiro</option><option value="LIC-A3-SESCSP_SG" >LIC-A3</option>';
      
      $(wrapper).append(fieldHTML);
      $('#field_uo_origem')
      .clone()
      .attr('id', 'field_uo_origem-'+x)
      .insertAfter($('[id^=id_field_email]:last'));
      const innerDiv = document.getElementById('field_uo_origem-'+x).querySelector('#field_uo_origem');
      //const innerDiv = document.getElementById('field_uo-'+x++)
      innerDiv.setAttribute("name","field_uo_origem["+x+"]")

      $($('#id_field_uo'))
      .clone()
      .attr('id', 'field_uo-'+x)
      .insertAfter($('[id^=field_uo_origem-'+x+']'));;
      console.log(x)
      const innerDiv2 = document.getElementById('field_uo-'+x).querySelector('#field_uo');
      innerDiv2.setAttribute("name","field_uo["+x+"]");
      x++;   
      document.getElementById('countField').value = x
    }
  });
  $(disableButton).click(function () {    
    if (x < maxField) {
      var fieldHTML = '<div class="row line'+x+'" ><div class="col-2 m-1"></div><div class="col m-1" id="id_field_email"> <input class="form-control" type="text" id="field_email" name="field_email['+x+']" value="" placeholder="nome.sobrenome" required="required"/> </div><div class="col-2 m-1"></div></div>';
      
      $(wrapper).append(fieldHTML);
      $('#id_field_uo')
      .clone()
      .attr('id', 'field_uo-'+x)
      .insertAfter($('[id^=id_field_email]:last'));
      const innerDiv = document.getElementById('field_uo-'+x).querySelector('#field_uo')
      //const innerDiv = document.getElementById('field_uo-'+x++)
      innerDiv.setAttribute("name","field_uo["+x+"]")
      x++;   
      document.getElementById('countField').value = x
    }
  });
  $(copyGroupButton).click(function () {    
    if (x < maxField) {
      var fieldHTML = '<div class="row line'+x+'" ><div class="col-2 m-1"></div><div class="col m-1" id="id_field_email"> <input class="form-control" type="text" id="field_email" name="field_email_base['+x+']" value="" placeholder="nome.sobrenome do usuário base" required="required"/> </div><div class="col m-1" id="id_field_email"> <input class="form-control" type="text" id="field_email" name="field_email_destino['+x+']" value="" placeholder="nome.sobrenome usuário destino" required="required"/> </div><div class="col-2 m-1"></div></div>';;
      
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
  
  $('#textAreaBtn').click(function() { 
    const element = document.querySelector('#textAreaCopy');
    element.select();
    element.setSelectionRange(0, 99999);
    document.execCommand('copy');
    document.getElementById("textAreaBtn").innerHTML = "Copiado!";
    
    
  ;}); 
  
  function TodayDate(){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();
    if(dd<10){
      dd='0'+dd;
    } 
    if(mm<10){
        mm='0'+mm;
    } 
    today = yyyy+'-'+mm+'-'+dd;                
    return today

  }
  

  var dataSearch = document.getElementById("datasearch")
  if (dataSearch !== null) {
    dataSearch.defaultValue =TodayDate()+"";
  }
  
  var textARea = document.getElementById('textAreaCopy')
  if (textARea !== null) {
    var content = textARea.value;
    if(content.length>20)
    {
      document.getElementById('textAreaCopy').style.display = "block";
      document.getElementById('textAreaBtn').style.display = "block";
    }
  }
  

});


