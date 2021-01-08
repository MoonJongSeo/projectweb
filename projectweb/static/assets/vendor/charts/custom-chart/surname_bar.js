var bar_chart = null;
function show_bar_chart(labels, datasets) {
    var ctx = $("#single_bar_chart");
    if (ctx) {
        ctx.height = 150;

        if (bar_chart) {
            bar_chart.destroy();
        }

        var bar_chart = new Chart(ctx, {
            type: 'bar',
            data: {
            labels: labels,
            datasets: [
                {
                label: "인구 분포",
                data: datasets,
                borderColor: "rgba(0, 123, 255, 0.9)",
                borderWidth: "0",
                backgroundColor: "rgba(0, 123, 255, 0.5)"
                }
            ]
            },
            options: {
            legend: {
                position: 'top',
                labels: {
                fontFamily: 'Poppins'
                }

            },
            scales: {
                xAxes: [{
                ticks: {
                    fontFamily: "Poppins"

                }
                }],
                yAxes: [{
                ticks: {
                    beginAtZero: true,
                    fontFamily: "Poppins"
                }
                }]
            }
            }
        });
    }
}