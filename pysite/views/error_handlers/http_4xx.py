# coding=utf-8
from flask import render_template, request
from werkzeug.exceptions import NotFound

from pysite.base_route import ErrorView
from pysite.constants import ERROR_DESCRIPTIONS


class Error400View(ErrorView):
    name = "error_4xx"
    error_code = range(400, 430)

    def get(self, error: NotFound):
        error_desc = ERROR_DESCRIPTIONS.get(error.code, "We're not really sure what happened there, please try again.")

        return render_template("errors/error.html", code=error.code, req=request, error_title=error_desc,
                               error_message=error_desc +
                               " If you believe we have made a mistake, "
                               "please open an issue "
                               "on our"
                               " <a href='https://github.com"
                               "/discord-python/site/issues'>GitHub</a>."), error.code
