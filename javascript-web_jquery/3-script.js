#!/usr/bin/node
$(document).ready(() => {
    $('DIV#red_header').on('click', () => {
      $('header').addClass('red');
    });
  });
