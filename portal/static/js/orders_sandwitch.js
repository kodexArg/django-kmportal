$(document).ready(function () {
    const pauseModal = $('#pause-modal');
    const viewModal = $('#view-modal');
    const pauseCloseModal = $('#pause-modal-close');
    const viewCloseModal = $('#view-modal-close');
    const formPause = $('#pause-form');
    let orderId;

    // Pause order functionality
    $('[id^="pause-button-"]').click(function () {
        orderId = $(this).data('order-id');

        $.ajax({
            url: `/orders/${orderId}/data/`,
            type: 'GET',
            success: function (data) {
                // Check if the order is already pauseed
                if (data.is_paused) {
                    $('button[value="pause"]').find('p').text('{% translate "btn_continue" %}');
                } else {
                    $('button[value="pause"]').find('p').text('{% translate "btn_pause" %}');
                }

                // Modify the form action attribute
                formPause.attr('action', `/orders/${orderId}/pause/`);

                // Display the modal
                pauseModal.toggleClass('opacity-0 invisible pointer-events-none');
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error('Error occurred while retrieving order data:', errorThrown);
            }
        });
    });

    // Close Pause Modal
    pauseCloseModal.click(function () {
        pauseModal.addClass('opacity-0 invisible pointer-events-none');
    });

    // Listen for form submit
    formPause.on('submit', function (e) {
        e.preventDefault(); // prevent the form from submitting normally

        // get the value of the action
        let action = $(this).find('button[type="submit"]:focus').val();

        let data = {
            'csrfmiddlewaretoken': $(this).find('input[name="csrfmiddlewaretoken"]').val(),
            'action': action,
        };

        $.ajax({
            url: `/orders/${orderId}/pause/`,
            type: 'POST',
            data: data,
            success: function (response) {
                console.log('Response from server: ', response);
                if (response.result == "success") {
                    pauseModal.addClass('opacity-0 invisible pointer-events-none');
                    location.reload();
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error('Error occurred while trying to pause/delete order:', errorThrown);
            }
        });
    });

    // View order functionality
    $('[id^="view-button-"]').click(function () {
        orderId = $(this).data('order-id');

        $.ajax({
            url: `/orders/${orderId}/data/`,
            type: 'GET',
            success: function (data) {
                // Update the order status text based on the order data
                let statusTextElement = $('#order-status-text');
                if (data.is_finished) {
                    statusTextElement.text('{% translate "finished" %}');
                    statusTextElement.removeClass('text-red-500 text-orange-500');
                    statusTextElement.addClass('text-green-500');
                } else if (data.is_paused) {
                    statusTextElement.text('{% translate "pauseed" %}');
                    statusTextElement.removeClass('text-green-500 text-orange-500');
                    statusTextElement.addClass('text-red-500');
                } else if (data.is_blocked) {
                    statusTextElement.text('{% translate "blocked" %}');
                    statusTextElement.removeClass('text-green-500 text-red-500');
                    statusTextElement.addClass('text-orange-500');
                } else {
                    statusTextElement.text('')
                }

                // This approach generates a URL with order_id as 0 and then replaces '0' with the actual orderId
                // because { % url.. % } line is generated serverside, and the javascript replaces it when the orderId variable
                // is ready.
                $('#qr_image img').attr('src', "{% url 'get_qr' order_id=0 %}".replace('0', orderId));
                $('#qr_image p').text(data.operation_code.toUpperCase());

                // Fill in the rest of the fields in the view modal
                $('#order_date').text(data.order_date);
                $('#modified_date').text(data.modified_date);
                $('#driver').text(data.driver);
                $('#tractor_plate').text(data.tractor_plate);
                $('#trailer_plate').text(data.trailer_plate);
                $('#formated_tractor_liters_to_load_of').text(data.formated_tractor_liters_to_load_of == 0 ? 'NO' : data.formated_tractor_liters_to_load_of == -1 ? 'MAX' : data.formated_tractor_liters_to_load_of);

                $('#formated_backpack_liters_to_load_of').text(data.formated_backpack_liters_to_load_of == 0 ? 'NO' : data.formated_backpack_liters_to_load_of == -1 ? 'MAX' : data.formated_backpack_liters_to_load_of);

                $('#formated_chamber_liters_to_load_of').text(data.formated_chamber_liters_to_load_of == 0 ? 'NO' : data.formated_chamber_liters_to_load_of == -1 ? 'MAX' : data.formated_chamber_liters_to_load_of);


                viewModal.toggleClass('opacity-0 invisible pointer-events-none');
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error('Error occurred while retrieving order data:', errorThrown);
            }
        });
    });



    // Close View Modal
    viewCloseModal.click(function () {
        viewModal.addClass('opacity-0 invisible pointer-events-none');
    });

    // Close modals on outside click
    $(window).click(function (event) {
        if (event.target == pauseModal[0]) {
            pauseModal.addClass('opacity-0 invisible pointer-events-none');
        } else if (event.target == viewModal[0]) {
            viewModal.addClass('opacity-0 invisible pointer-events-none');
        }
    });

});