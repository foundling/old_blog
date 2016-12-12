#!/usr/bin/env

from app import blog

if __name__ == '__main__':

    blog.run(

        host='0.0.0.0',
        debug=True,

    )
