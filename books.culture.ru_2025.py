from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests


authors_en = ['nikolay-ostrovskiy', 'aleksandr-grin', 'afanasii-fet', 'leonid-andreev', 'ivan-dmitriev', 'dmitriy-mamin-sibiryak', 'vladimir-odoevskii', 'nikolai-nekrasov', 
              'evgeniy-zamyatin', 'dmitrii-venevitinov', 'aleksandr-radishev', 'sasha-chernyi', 'ivan-krylov', 'eduard-bagritskiy', 'dmitriy-furmanov', 'vasilii-zhukovskii', 'dmitriy-pisarev', 'lev-tolstoi', 'fedor-sologub', 'aleksandr-griboedov', 'maksim-gorkii', 'nikolai-gogol', 'fedor-glinka', 'aleksey-apuhtin', 'evgenii-boratynskii-baratynskii', 'anton-chekhov', 'nikolai-leskov', 'vsevolod-krestovskiy', 'gleb-uspenskiy', 'ivan-turgenev', 'aleksandr-veltman', 'andrei-belyi', 'vsevolod-garshin', 'aleksey-pisemskiy', 'dmitriy-grigorovich', 'nikolay-pomyalovskiy', 'aleksandr-kuprin', 'aleksandr-gertsen', 'sergei-esenin', 'aleksei-plesheev', 'aleksei-tolstoi', 'aleksandr-ostrovskii', 'nikolai-chernyshevskii', 'nikolai-karamzin', 'vladimir-dal', 'mikhail-lermontov', 'sergei-aksakov', 'nikolay-garin-mihaylovskiy', 'kondratiy-rileev', 'vladimir-sollogub', 'fedor-dostoevskii', 'aleksandr-pushkin', 'fedor-tyutchev', 'vladimir-gilyarovskiy', 'mikhail-saltykov-shedrin', 'aleksandr-blok', 'denis-fonvizin', 'vladimir-korolenko', 'ivan-goncharov', 'petr-ershov', 'daniil-mordovtsev', 'mihail-zagoskin', 'aleksei-konstantinovich-tolstoi', 'velimir-hlebnikov', 'antoniy-pogorelskiy', 'orest-somov']
authors_ru = ['Николай Островский', 'Александр Грин', 'Афанасий Фет', 'Леонид Андреев', 'Иван Дмитриев', 'Дмитрий Мамин-Сибиряк', 'Владимир Одоевский', 'Николай Некрасов', 
              'Евгений Замятин', 'Дмитрий Веневитинов', 'Александр Радищев', 'Саша Черный', 'Иван Крылов', 'Эдуард Багрицкий', 'Дмитрий Фурманов', 'Василий Жуковский', 'Дмитрий Писарев', 'Лев Толстой', 'Федор Сологуб', 'Александр Грибоедов', 'Максим Горький', 'Николай Гоголь', 'Федор Глинка', 'Алексей Апухтин', 'Евгений Боратынский (Баратынский)', 'Антон Чехов', 'Николай Лесков', 'Всеволод Крестовский', 'Глеб Успенский', 'Иван Тургенев', 'Александр Вельтман', 'Андрей Белый', 'Всеволод Гаршин', 'Алексей Писемский', 'Дмитрий Григорович', 'Николай Помяловский', 'Александр Куприн', 'Александр Герцен', 'Сергей Есенин', 'Алексей Плещеев', 'Алексей Толстой', 'Александр Островский', 'Николай Чернышевский', 'Николай Карамзин', 'Владимир Даль', 'Михаил Лермонтов', 'Сергей Аксаков', 'Николай Гарин-Михайловский', 'Кондратий Рылеев', 'Владимир Соллогуб', 'Федор Достоевский', 'Александр Пушкин', 'Федор Тютчев', 'Владимир Гиляровский', 'Михаил Салтыков-Щедрин', 'Александр Блок', 'Денис Фонвизин', 'Владимир Короленко', 'Иван Гончаров', 'Петр Ершов', 'Даниил Мордовцев', 'Михаил Загоскин', 'Алексей Толстой', 'Велимир Хлебников', 'Антоний Погорельский', 'Орест Сомов']

def getContent(url):
    session = get_session()
    headers = {

        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'cookie': '_ym_uid=1736239670404857305; _ym_d=1736239670; cookieUsageDisclaimer=true; popupDelay146=true; _ym_isad=2; _ym_visorc=b',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    try:
        data = session.get(url, headers=headers)
        text = data.text
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(text, 'html.parser')
        content = bs.find('div', {'class': 'container container__pvi-no-styles container__medium'} ).find('div', {'class': 'section_body'})
        pagination = bs.find('nav', {'class': 'pagination'}).find_all('a')
        print(pagination)
        pagination_list = []
        for a in pagination:
            end_link = a.attrs.get('href')
            full_link = 'https://www.culture.ru/' + end_link
            pagination_list.append(full_link)
            pass
        print(pagination_list)

    except AttributeError as e:
        return None
    # Настроить возврат страницы с учетом пагинации
    return content


def get_session():
    s = requests.Session()
    return s


def make_address(name_en):
    name_en = name_en.replace(' ', '-')
    address = 'https://www.culture.ru/literature/books/author-' + name_en
    return address


def main():
    for name_en in authors_en:
        address = make_address(name_en)
        print(address + '\n')
        if name_en == 'aleksandr-grin':
            content = getContent(address)
            if content == None:
                print('Content could not be found\n')
            else:
                # print(content, '\n')
                print('OK\n')
                # anchors = content.find_all('href')
                for a_tag in content.find_all("a"):
                    href = a_tag.attrs.get("href")
                    if href == "" or href is None:
            # href пустой тег
                        continue
                    else:
                        # делаю ссылку на книгу
                        href_full = 'https://www.culture.ru/' + href
                        # Печатаю ссылку на книгу
                        print(href_full)
                        url = href_full
                        response = requests.get(url).status_code
                        print(response)
                        bad_url_list = []
                        if response == 200:
                            book_page = requests.get(url)
                            text = book_page.text
                            # print(text)
                            bs = BeautifulSoup(text, 'html.parser')
                            book_title = bs.find('h1').get_text()
                            print(book_title)
                            book_auther = bs.find('a', {'class': 'attributes_value'}).get_text()
                            print(book_auther)
                            book_link = bs.find('a', {'class':'about-entity_btn button button__primary'}).find_next('a')
                            file_link = book_link.attrs.get('href')
                            print(book_link)
                            print(file_link)
                            file_name = book_auther + '. ' + book_title + '.epub'
                            print(file_name)
                            url = file_link
                            response = requests.get(url)
                            with open(file_name, 'wb') as file:
                                file.write(response.content)
                        else:
                            bad_url_list.append(url)
                    print('BAD URL', bad_url_list)

                        # <a href="https://cdn.culture.ru/files/2855c1ed-5a02-5d07-a525-d4cdaaaf3462/zelenaya-lampa" class="about-entity_btn button button__primary">Скачать книгу</a>
        # content = bs.find('div', {'class': 'container container__pvi-no-styles container__medium'} ).find('div', {'class': 'section_body'})




if "__name__" == "__name__":
    main()
