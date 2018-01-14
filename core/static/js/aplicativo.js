$(document).ready(function() {
    // permite que o usuario selecione alguma alternativa na caixa de seleção //
    $('select').material_select();
    // modal de exclusão de cadastros //
    $('.modal').modal();
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('#modal2').modal('open');
    $('#modal3').modal();
});


/* Slide down and up de botões barra lateral */
$('.master-menu').click(function(e){
  e.preventDefault();
  $(this).next('ul').slideToggle();
  $('.child-menu').not($(this).next()).slideUp();
});

/* Barra lateral posicionada e seu tamanho definido */
$('.button-collapse').sideNav({
    menuWidth: 300, // Default is 300
    edge: 'left', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true // Choose whether you can drag to open on touch screens
  }
);

// Configuração e tradução do calendário datepicker materialize
$('.datepicker').pickadate({
  dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
  monthsFull: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
  monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
  weekdaysFull: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
  weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
  weekdaysLetter: [ 'D', 'S', 'T', 'Q', 'Q', 'S', 'S' ],
  today: 'Hoje',
  clear: 'Limpar',
  close: 'ok',
  labelMonthNext: 'Próximo mês',
  labelMonthPrev: 'Mês anterior',
  labelMonthSelect: 'Selecione um mês',
  labelYearSelect: 'Selecione um ano',
  selectMonths: true,
  selectYears: 70,
  container: 'body',
  // format: 'dd-mm-yyyy'
  format: 'yyyy-mm-dd',
  // max: ['0']
  max:['0']
});
