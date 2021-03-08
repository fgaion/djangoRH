function teste(){
    alert("beleza!");
}

function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    //exemplo de como pegar outro paramenbtro - ver registrohoraextra_form.html
    //valor = document.getElementById("CampoX").value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            //outro_param: valor
        },
        success: function(result){
            console.log(result);
            //$("#mensagem").text('Hora extra Marcada como realizada');
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}


function process_response(funcionarios){
    func_select = document.getElementById('funcionarios');
    func_select.innerHTML = "";

    funcionarios.forEach(function(funcionario){
        var option = document.createElement("option");
        option.text = funcionario.fields.nome;
        func_select.add(option);
    });
}

function filtraFuncionarios(){
    depart_id = document.getElementById('departamentos').value;
    $.ajax({
        type: 'GET',
        url: '/filtra-funcionarios/',
        data: {
            outro_param: depart_id
        },
        success: function(result){
            process_response(result);
            $("#mensagem").text('Funcionarios carregados');
        }
    });
}
