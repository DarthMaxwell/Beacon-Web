from django.shortcuts import render
from django.http import HttpResponse
from splash.models import Beacons, Beacon_Reading
from django.db.models import Count

beacons = Beacons.objects.all()

beaconlist = "<table class=\"table\">"
for beacon in beacons:
    beaconlist = beaconlist + "<tr><td>" + str(beacon.beacon_id) + "</td>"
    beaconlist = beaconlist + "<td>" + beacon.beacon_string + "</td></tr>"
beaconlist =  beaconlist + "</table>"

querycounts = Beacon_Reading.objects.values("beacon_id").annotate(Count("beacon_id")).order_by()
beaconcounts = ""
for querycount in querycounts:
    print(querycount)
    beaconcounts = beaconcounts + "," + str(querycount['beacon_id__count'])

hello = "<link rel=\"shortcut icon\" type=\"image/png\" href=\"/favicon.ico\"/>Hello, world.<br>"

template = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>One Page Wonder - Start Bootstrap Template</title>

    <!-- Bootstrap Core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="/static/css/one-page-wonder.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>

</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">MARTA Beacons</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="#about">About</a>
                    </li>
                    <li>
                        <a href="#services">Services</a>
                    </li>
                    <li>
                        <a href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Full Width Image Header -->
    <header class="header-image">
	
        <div class="headline">
            <div class="container">
                <h1>Team H MARTABeacons</h1>
                <h2>A new way of navigation and advertisement</h2>
            </div>
        </div>
    </header>

    <!-- Page Content -->
    <div class="container">

        <hr class="featurette-divider">

        <div class="featurette" id="beacon-list">
        """ + beaconlist + """
        </div>

        <!-- First Featurette -->
        <div class="featurette" id="about">
            <img class="featurette-image img-circle img-responsive pull-right" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Raspberry-Pi-2-Bare-FL.jpg">
            <h2 class="featurette-heading">Bluetooth Beacons
                <span class="text-muted">for Navigation, Advertising, and Emergency Rsponse</span>
            </h2>
            <p class="lead">Placed at strategic points around MARTA stations, our bluetooth beacons have many uses. MARTA will know more about their foot traffic and be able to fine toon advertising. In addition emercencies </p>
        </div>

        <hr class="featurette-divider">

        <!-- Second Featurette -->
        <div class="featurette" id="services">
            <h2 class="featurette-heading">Realtime Data
                <span class="text-muted">Number of People by each Beacon</span>
            </h2>
            <p class="lead">Below is a live pie chart of the number of devices near each beacon(every beacon is a different color).</p>
            <canvas id="myChart" width="400" height="400" class="pull-left"></canvas>
        </div>

        <hr class="featurette-divider">

        <!-- Third Featurette -->
        <div class="featurette" id="contact">

            <img class="featurette-image img-circle img-responsive pull-right" src="https://lh3.googleusercontent.com/-gI8isMMwQ7Q/WLHufVEMn5I/AAAAAAAAB2w/glTOpv2c7kc6aMPtIHjrMLrUMxf_j5SXQCL0B/h439/2017-02-25.png">
            <h2 class="featurette-heading">The

                <span class="text-muted">Squad</span>
            </h2>
            <p class="lead">Our team! We had a great time. Thanks to MARTA and everyone else for this opportunity.</p>
        </div>

        <hr class="featurette-divider">

        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12">
                    <p>Copyright &copy; MARTA Beacons 2017</p>
                </div>
            </div>
        </footer>

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="/static/js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="/static/js/bootstrap.min.js"></script>

    <script>
    var ctx = document.getElementById("myChart");
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Beacon 1", "Beacon 2", "Beacon 3", "Beacon 4", "Beacon 5", "Beacon 6"],
            datasets: [{
                label: 'people',
                data: [""" + beaconcounts +"""],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    </script>

</body>

</html>
"""

def index(request):
    return HttpResponse(template)
