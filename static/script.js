function buscarGit(){
    console.log('Buscando git!');
    let usuario = document.getElementById('input_git').value;
    
    fetch('http://127.0.0.1:5000/github?usuario=' + usuario)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data.message){
                window.alert('Houve um erro ao buscar usuario: ' + data.message);
                return
            }
            document.getElementById('foto_git').setAttribute('src', data.foto);
            document.getElementById('nome_git').innerText = data.nome;
            document.getElementById('usuario_git').innerText = data.usuario;
            document.getElementById('bio_git').innerText = data.bio;
            document.getElementById('location_git').innerText = data.local;
        }).catch(error => {
            console.log('Erro: ' + error);
            window.alert('Houve um erro ao mostrar usuario');
        });
}

function buscarFilme(){
    console.log('Buscando filme!');
    let filme = document.getElementById('input_filme').value;
    fetch('http://127.0.0.1:5000/searchfilme?filme=' + filme)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data.message){
                window.alert('Erro ao buscar filme: ' + data.message);
                return
            }
            document.getElementById('foto_filme').setAttribute('src', data.foto);
            document.getElementById('nome_filme').innerText = data.titulo;
            document.getElementById('data_filme').innerText = data.data;
            document.getElementById('nota_filme').innerText = data.nota;
            document.getElementById('descricao_filme').innerText = data.descricao;
            document.getElementById('foto_similar_1').setAttribute('src', data.similar[0].foto);
            document.getElementById('nome_similar_1').innerText = data.similar[0].titulo;
            document.getElementById('foto_similar_2').setAttribute('src', data.similar[1].foto);
            document.getElementById('nome_similar_2').innerText = data.similar[1].titulo;
            document.getElementById('foto_similar_3').setAttribute('src', data.similar[2].foto);
            document.getElementById('nome_similar_3').innerText = data.similar[2].titulo;
        }).catch(error => {
            console.log('Erro: ' + error);
            window.alert('Houve um erro ao mostrar filme');
        });
}