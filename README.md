# geolocalizer

Uruchomienie
--------------
w terminalu w katalogu głównym projektu należy wydac polecenie
docker-compose up

Użytkowanie
--------------
dostępne endpointy:
 
 1) Zarządzanie autoryzacją (djoser):
      /auth/users/
      /auth/users/me/
      /auth/users/confirm/
      /auth/users/resend_activation/
      /auth/users/set_password/
      /auth/users/reset_password/
      /auth/users/reset_password_confirm/
      /auth/users/set_username/
      /auth/users/reset_username/
      /auth/users/reset_username_confirm/
      /auth/jwt/create/ (JSON Web Token Authentication)
      /auth/jwt/refresh/ (JSON Web Token Authentication)
      /auth/jwt/verify/ (JSON Web Token Authentication)
    
  2) Geolokalizacja
      /geoloc/geolocalizations/
      /geoloc/geolocalizations/{ip/url}
