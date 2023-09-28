from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def root():
    return render_template("base.html")


@app.get("/clothes/")
def clothes():
    clothes_list = [
        {
            "photo": "https://tvoe.ru/img/3met1lm/product/626/834/36/4620123842125-2.jpg",
            "name": "ХЛОПКОВАЯ ФУТБОЛКА С НАДПИСЬЮ НА СПИНЕ",
            "cost": "1 999 P",
        },
        {
            "photo": "https://tvoe.ru/img/1d8clh4/product/754/1005/8/4620123842620.jpg",
            "name": "ХЛОПКОВЫЙ ЛОНГСЛИВ В ПОЛОСКУ",
            "cost": "1 499 P",
        },
    ]
    return render_template("clothes.html", clothes_list=clothes_list)


@app.get("/jackets/")
def jackets():
    jacket_list = [
        {
            "photo": "https://tvoe.ru/img/2a2vmjg/product/626/834/36/4620123716044-2.jpg",
            "name": "КУРТКА ПУХОВИК БЕЗ КАПЮШОНА",
            "cost": "3 999 P",
        },
        {
            "photo": "https://tvoe.ru/img/2hmfm3t/product/626/834/36/4620123715948-2.jpg",
            "name": "КУРТКА ПУХОВИК БЕЗ КАПЮШОНА",
            "cost": "3 899 P",
        },
    ]
    return render_template("jacket.html", jacket_list=jacket_list)


@app.route("/shoes/")
def shoes():
    shoes_list = [
        {
            "photo": "https://tvoe.ru/img/2tfslts/product/626/834/36/4620123766308-2.jpg",
            "name": "ВЫСОКИЕ КРОССОВКИ НА БЕЛОЙ ПОДОШВЕ",
            "cost": "2 379 Р",
        },
         {
            "photo": "https://tvoe.ru/img/22nr5sg/product/754/1005/8/4620123718482.jpg",
            "name": "КРОССОВКИ НА ТОЛСТОЙ ПОДОШВЕ",
            "cost": "1 619 Р",
        },
        
    ]
    return render_template("shoes.html", shoes_list=shoes_list)


if __name__ == "__main__":
    app.run(debug=True)