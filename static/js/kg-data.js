$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Strike Price
    var strike_price_min = parseInt($('#strike_price_min').val(), 10);
    var strike_price_max = parseInt($('#strike_price_max').val(), 10);
    var strike_price = parseFloat(data[4]) || 0; // use data for the age column
    if (
        (isNaN(strike_price_min) && isNaN(strike_price_max)) ||
        (isNaN(strike_price_min) && strike_price <= strike_price_max) ||
        (strike_price_min <= strike_price && isNaN(strike_price_max)) ||
        (strike_price_min <= strike_price && strike_price <= strike_price_max)
    ) {
        return true;
    }

    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();
 
    // Event listener to the two range filtering inputs to redraw on input
    $('#strike_price_min, #strike_price_max').keyup(function () {
        table.draw();
    });

    
});

// For Last Price Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var last_price_min = parseInt($('#last_price_min').val(), 10);
    var last_price_max = parseInt($('#last_price_max').val(), 10);
    var last_price = parseFloat(data[5]) || 0; // use data for the age column
    if (
        (isNaN(last_price_min) && isNaN(last_price_max)) ||
        (isNaN(last_price_min) && last_price <= last_price_max) ||
        (last_price_min <= last_price && isNaN(last_price_max)) ||
        (last_price_min <= last_price && last_price <= last_price_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#last_price_min, #last_price_max').keyup(function () {
        table.draw();
    });
});


// For Price Change Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var price_change_min = parseInt($('#price_change_min').val(), 10);
    var price_change_max = parseInt($('#price_change_max').val(), 10);
    var price_change = parseFloat(data[6]) || 0; // use data for the age column
    if (
        (isNaN(price_change_min) && isNaN(price_change_max)) ||
        (isNaN(price_change_min) && price_change <= price_change_max) ||
        (price_change_min <= price_change && isNaN(price_change_max)) ||
        (price_change_min <= price_change && price_change <= price_change_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#price_change_min, #price_change_max').keyup(function () {
        table.draw();
    });
});

// For Price Change Percentage Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var price_change_per_min = parseInt($('#price_change_per_min').val(), 10);
    var price_change_per_max = parseInt($('#price_change_per_max').val(), 10);
    var price_change_per = parseFloat(data[7]) || 0; // use data for the age column
    if (
        (isNaN(price_change_per_min) && isNaN(price_change_per_max)) ||
        (isNaN(price_change_per_min) && price_change_per <= price_change_per_max) ||
        (price_change_per_min <= price_change_per && isNaN(price_change_per_max)) ||
        (price_change_per_min <= price_change_per && price_change_per <= price_change_per_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#price_change_per_min, #price_change_per_max').keyup(function () {
        table.draw();
    });
});

// For High Value Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var high_value_min = parseInt($('#high_value_min').val(), 10);
    var high_value_max = parseInt($('#high_value_max').val(), 10);
    var high_value = parseFloat(data[8]) || 0; // use data for the age column
    if (
        (isNaN(high_value_min) && isNaN(high_value_max)) ||
        (isNaN(high_value_min) && high_value <= high_value_max) ||
        (high_value_min <= high_value && isNaN(high_value_max)) ||
        (high_value_min <= high_value && high_value <= high_value_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#high_value_min, #high_value_max').keyup(function () {
        table.draw();
    });
});

// For Low Value Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var min_low_min = parseInt($('#min_low_min').val(), 10);
    var min_low_max = parseInt($('#min_low_max').val(), 10);
    var min_low = parseFloat(data[9]) || 0; // use data for the age column
    if (
        (isNaN(min_low_min) && isNaN(min_low_max)) ||
        (isNaN(min_low_min) && min_low <= min_low_max) ||
        (min_low_min <= min_low && isNaN(min_low_max)) ||
        (min_low_min <= min_low && min_low <= min_low_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#min_low_min, #min_low_max').keyup(function () {
        table.draw();
    });
});


// For Option Value Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var min_option_min = parseInt($('#min_option_min').val(), 10);
    var min_option_max = parseInt($('#min_option_max').val(), 10);
    var min_option = parseFloat(data[10]) || 0; // use data for the age column
    if (
        (isNaN(min_option_min) && isNaN(min_option_max)) ||
        (isNaN(min_option_min) && min_option <= min_option_max) ||
        (min_option_min <= min_option && isNaN(min_option_max)) ||
        (min_option_min <= min_option && min_option <= min_option_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#min_option_min, #min_option_max').keyup(function () {
        table.draw();
    });
});

// For Open Interest Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var oi_min_min = parseInt($('#oi_min_min').val(), 10);
    var oi_min_max = parseInt($('#oi_min_max').val(), 10);
    var oi_min = parseFloat(data[11]) || 0; // use data for the age column
    if (
        (isNaN(oi_min_min) && isNaN(oi_min_max)) ||
        (isNaN(oi_min_min) && oi_min <= oi_min_max) ||
        (oi_min_min <= oi_min && isNaN(oi_min_max)) ||
        (oi_min_min <= oi_min && oi_min <= oi_min_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#oi_min_min, #oi_min_max').keyup(function () {
        table.draw();
    });
});


// For Open Int Cahnge Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var oi_change_min = parseInt($('#oi_change_min').val(), 10);
    var oi_change_max = parseInt($('#oi_change_max').val(), 10);
    var oi_change = parseFloat(data[12]) || 0; // use data for the age column
    if (
        (isNaN(oi_change_min) && isNaN(oi_change_max)) ||
        (isNaN(oi_change_min) && oi_change <= oi_change_max) ||
        (oi_change_min <= oi_change && isNaN(oi_change_max)) ||
        (oi_change_min <= oi_change && oi_change <= oi_change_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#oi_change_min, #oi_change_max').keyup(function () {
        table.draw();
    });
});


// For Open Int Change Percentage Filter

$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
    
    // For Last Price
    var oi_change_per_min = parseInt($('#oi_change_per_min').val(), 10);
    var oi_change_per_max = parseInt($('#oi_change_per_max').val(), 10);
    var oi_change_per = parseFloat(data[13]) || 0; // use data for the age column
    if (
        (isNaN(oi_change_per_min) && isNaN(oi_change_per_max)) ||
        (isNaN(oi_change_per_min) && oi_change_per <= oi_change_per_max) ||
        (oi_change_per_min <= oi_change_per && isNaN(oi_change_per_max)) ||
        (oi_change_per_min <= oi_change_per && oi_change_per <= oi_change_per_max)
    ) {
        return true;
    }


    return false;
});
 
$(document).ready(function () {
    var table = $('#kg_table').DataTable();

    $('#oi_change_per_min, #oi_change_per_max').keyup(function () {
        table.draw();
    });
});