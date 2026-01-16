from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_musicas = []
artistas = []
ouvintes = []

generos = ("Samba", "Rock", "Sertanejo", "Pop", "Jazz", "Funk")

# ---------------- ROTAS ---------------- #

@app.route("/")
def index():
    return render_template('index.html')


# ADICIONAR MUSICA
@app.route("/adicionarMusica", methods=["GET", "POST"])
def adicionar_musica():
    if request.method == "POST":
        nome = request.form["musica"]

        # Adiciona apenas se não existir
        if nome not in lista_musicas:
            lista_musicas.append(nome)

        return redirect(url_for("listar_musica"))
    return render_template('adicionar.html')


# EDITAR MUSICA
@app.route("/editarMusica", methods=["GET", "POST"])
def editar_musica():
    if request.method == "POST":
        antiga = request.form["musica"]
        nova = request.form["nova_musica"]

        if antiga in lista_musicas:
            index_musica = lista_musicas.index(antiga)
            lista_musicas[index_musica] = nova

        return redirect(url_for("listar_musica"))
    return render_template('editar.html')


# EXCLUIR MUSICA
@app.route('/excluirMusica', methods=["GET", "POST"])
def excluir_musica():
    if request.method == "POST":
        nome = request.form["musica"]

        if nome in lista_musicas:
            lista_musicas.remove(nome)

        return redirect(url_for("listar_musica"))
    return render_template('excluir.html')


# PLAYLIST
@app.route('/playlist')
def listar_musica():
    return render_template('playlist.html', lista_musicas=lista_musicas)


# CADASTRAR ARTISTA
@app.route('/cadastrarArtista', methods=["GET", "POST"])
def cadastrar_artista():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        idade = request.form["idade"]
        genero = request.form["genero"]
        musicas = request.form["musicas"].split(",")

        # Remove espaços soltos
        musicas = [m.strip() for m in musicas if m.strip()]

        # SALVAR NO BANCO DE ARTISTAS
        artistas.append({
            "nome": nome,
            "email": email,
            "idade": idade,
            "genero": genero,
            "musicas": musicas
        })

        # ADICIONAR NA PLAYLIST GLOBAL
        for m in musicas:
            if m not in lista_musicas:
                lista_musicas.append(m)

        return redirect(url_for("index"))

    return render_template('cadastrar_artista.html', generos=generos)


# CADASTRAR OUVINTE
@app.route('/cadastrarOuvinte', methods=["GET", "POST"])
def cadastrar_ouvinte():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        idade = request.form["idade"]
        genero = request.form["genero"]
        playlist = request.form["musicas"].split(",")
        favoritos = request.form["favoritos"].split(",")

        # Limpar espaços
        playlist = [m.strip() for m in playlist if m.strip()]
        favoritos = [m.strip() for m in favoritos if m.strip()]

        ouvintes.append({
            "nome": nome,
            "email": email,
            "idade": idade,
            "genero": genero,
            "playlist": playlist,
            "favoritos": favoritos
        })

        # ADICIONAR NA PLAYLIST GLOBAL
        for m in playlist + favoritos:
            if m not in lista_musicas:
                lista_musicas.append(m)

        return redirect(url_for("index"))

    return render_template("cadastrar_ouvinte.html", generos=generos)


if __name__ == "__main__":
    app.run(debug=True)
