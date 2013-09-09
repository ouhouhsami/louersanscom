LouerSansCom
============

Local dev
=========

run workers
* python manage.py rqworker default

mails sended by the application are in messages folder during development.

Other
=====

* activate contact@louersanscom.com
* dynamic flatpages
* moderation mails with custom styles

* comprendre pourquoi ressc va chercher dans perso/dev/bootstrap
* installer ressc sur le serveur de prod
* voir si on peut supprimer smartextends
* mettre a jour mail_factory sur django-geoads

Remarks
=======

3 configuration level:
* generic geoads (only views)
* bootstrap style + crispy_forms (sanscom app)
* site specific (instance louersanscom or achetersanscom)