import requests

class Axe:
    def visit_website(self):
        url = "https://itcollege.lviv.ua/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Website visited successfully!")
                # Якщо вам потрібно обробити вміст сторінки, ви можете використати response.text або інші методи
                # Наприклад, для виведення вмісту сторінки можна використати наступний рядок:
                # print(response.text)
            else:
                print(f"Failed to visit website. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Тестуємо метод visit_website:
if __name__ == "__main__":
    axe = Axe()
    axe.visit_website()