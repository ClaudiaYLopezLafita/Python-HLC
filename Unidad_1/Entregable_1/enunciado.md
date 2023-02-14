El Web Scrapping o "raspado web", es una técnica utilizada mediante programas de software para extraer información de sitios web. Estos programas simulación la navegación de un humano mediante peticiones HTTP (requests).

Vamos a realizar el scrapping de la web de películas filmaffinity. Concretamente de una película, pero podría valer para cualquier película, ya que se utiliza el mismo formato.

En la ficha de una película de filmaffinity se muestran diversos campos (en algunas películas, estos campos no aparecen, tendremos que tenerlo en cuenta):

    Título original
    Año
    Duración
    País
    Dirección
    Guión
    Música
    Fotografía
    Reparto
    Productora
    Género
    Sinopsis

Deberemos realizar un script en python que rastree toda la información de una película (se dará un ejemplo a seguir de como deberá quedar), y cada ítem que se pide, deberá hacerse en una función, que recibirá la web entera, y devolverá solamente el valor del ítem que se pide. Deberá construirse al final un diccionario con todos los ítems.