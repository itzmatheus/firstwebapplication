$(document).ready(function() {
    // permite que o usuario selecione alguma alternativa na caixa de seleção //
    $('select').material_select();
    // modal de exclusão de cadastros //
    $('.modal').modal();
    // Modal Error Nos Formulários
    $('#modal2').modal('open');
    $('#modal3').modal('open');
});

// Personalização de modal
$('.modal').modal({
    dismissible: true, // Modal can be dismissed by clicking outside of the modal
    opacity: .5, // Opacity of modal background
    inDuration: 300, // Transition in duration
    outDuration: 200, // Transition out duration
    startingTop: '4%', // Starting top style attribute
    endingTop: '10%', // Ending top style attribute
    ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
      alert("Ready");
      console.log(modal, trigger);
    },
    complete: function() { alert('Closed'); } // Callback for Modal close
  }
);

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
  selectMonths: true,
  selectYears: 70,
  // Título dos botões de navegação
  labelMonthNext: 'Próximo Mês',
  labelMonthPrev: 'Mês Anterior',
  // Título dos seletores de mês e ano
  labelMonthSelect: 'Selecione o Mês',
  labelYearSelect: 'Selecione o Ano',
  // Meses e dias da semana
  monthsFull: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
  monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
  weekdaysFull: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
  weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
  // Letras da semana
  weekdaysLetter: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
  //Botões
  today: 'Hoje',
  clear: 'Limpar',
  close: 'Ok',
  // Formato da data que aparece no input
  format: 'dd/mm/yyyy',
  max:['0'],
  onClose: function() {
    $(document.activeElement).blur()
  }
});
// $('.datepicker').pickadate({
//   dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
//   monthsFull: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
//   monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
//   weekdaysFull: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
//   weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
//   weekdaysLetter: [ 'D', 'S', 'T', 'Q', 'Q', 'S', 'S' ],
//   today: 'Hoje',
//   clear: 'Limpar',
//   close: 'ok',
//   labelMonthNext: 'Próximo mês',
//   labelMonthPrev: 'Mês anterior',
//   labelMonthSelect: 'Selecione um mês',
//   labelYearSelect: 'Selecione um ano',
//   selectMonths: true,
//   selectYears: 70,
//   container: 'body',
//   // format: 'dd-mm-yyyy'
//   format: 'yyyy-mm-dd',
//   // max: ['0']
//   max:['0']
// });
