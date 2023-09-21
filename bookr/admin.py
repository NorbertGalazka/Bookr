from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Aplikacja administacyjna 1 '
    site_header = 'Aplikacja administacyjna 2'
    index_title = 'Aplikacja administacyjna 3'