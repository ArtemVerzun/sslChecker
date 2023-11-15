## sslChecker
### Скрипт определяющий версии SSL на сервере и домены, указанные в SSL сертификате.
Входные данные берутся из текстового файла:
(на второй строке указан ненастоящий хост)

![image](https://github.com/ArtemVerzun/sslChecker/assets/143192676/cb29c645-51c6-4d15-9a8c-a394179f4df1)

Результат работы:
БД

![image](https://github.com/ArtemVerzun/sslChecker/assets/143192676/e098c13e-85b2-4d5d-82cc-00b42b8e76f3)

Консоль

![image](https://github.com/ArtemVerzun/sslChecker/assets/143192676/84b845a2-3550-48bd-b7c5-6463c158eaba)

Также добавлена проверка на дубликаты записей, при второй попытке записи данных в БД не создадутся такие же записи:

![image](https://github.com/ArtemVerzun/sslChecker/assets/143192676/65997d34-5ebc-4414-8bdf-20e58170b1f9)



