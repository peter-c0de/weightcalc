from data import Data

def manipulate_jscode(access):
    
    css_code = r"""
<style>

    h2{
        color: red;
    }

    h3{
        color: purple;
    }

    .h3_black{
        color: black;
    }

    .h3_red{
        color: red;
    }

    tr{
        /* Change it to change the cell's height size */
        line-height: 20px;
    }

    .float-container {
        /* border: 1px solid black; */
        margin: 1rem;
        padding: 2rem 2rem;
        text-align: center;
    }

    .float-child {
        display: inline-block;
        border: 1px solid red;
        padding: 1rem 1rem;
        vertical-align: middle;
    }

</style>
    """
    
    js_code = rf"""
<script type="text/javascript">
        function add_number() 
        {{
            //Change it every week.
            //---------- 4/4 Change Here: Week Starting Weight ---------->
            var week_starting = {access.starting_current_week}; 

            /*
            var current_weight = parseInt(document.getElementById("txt_current_weight").value);
            var week_result = week_starting - current_weight;
            week_result = week_result.toFixed(2) +" KGs";
            var result = 108.2 - current_weight;
            result = result.toFixed(2) +" KGs";
            */

            // Very IMP: USE ParseFLOAT instead of PARSEINT!!!!
            // VERY IMP: TO GET THE PERCESION RIGHT DO IT AS FOLLOWS:
            // Ref: https://stackoverflow.com/questions/1458633/how-to-deal-with-floating-point-number-precision-in-javascript
            var current_weight = parseFloat(document.getElementById("txt_current_weight").value);
            var week_result = parseFloat((week_starting - current_weight).toFixed(2));
            week_result = week_result +" KGs";

            // Starting Weight: 105.50
            var result = parseFloat((105.50 - current_weight).toFixed(2));
            result = result +" KGs";            

            //document.getElementById("txtresult").value = result;
            document.getElementById("lbl_week_loss").innerHTML = week_result ;
            document.getElementById("lbl_result").innerHTML = result ;
        }}
</script>
    """
    
    html_code = rf"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <link rel="icon" href="diet_ico.png" type="image/x-icon"/> -->
    <link rel="icon" href="diet.png" type="image/x-icon"/>
    <title>My Weight Progress</title>

    {css_code}

</head>
<body>  <div class="float-container">
        <div class="float-child">
            <h2>My Weight Progress</h2>
            <table>
                <tr>
                    <td><h3>Starting Date</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.starting_date}</h3></td>
                </tr>
                <tr>
                    <td><h3>Starting Weight</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.starting_weight}</h3></td>
                </tr>
                <tr>
                    <td><h3>First Month</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.first_month}</h3></td>
                </tr>
                <tr>
                    <td><h3>Second Month</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.second_month}</h3></td>
                </tr>
                <tr>
                    <td><h3>Third Month</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.third_month}</h3></td>
                </tr>
                <tr>
                    <td><h3>Fourth Month</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.fourth_month}</h3></td>
                </tr>
                <tr>
                    <td><h3>Fifth Month</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.fifth_month}</h3></td>
                </tr>
                <tr>
                    <!---------- 1/4 Change Here: Week Number ---------->
                    <!---------- 2/4 Change Here: Week KGs    ---------->
                    <td><h3>Starting Week {access.this_week_number}</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_black">{access.starting_current_week} KGs</h3></td>
                </tr>
                <tr>
                    <!---------- 3/4 Change Here: Week Number ---------->
                    <td><h3>Week {access.this_week_number} Loss</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_red"><label id="lbl_week_loss" name="lbl_week_loss"></label></h3></td>
                </tr>
                <tr>
                    <td><h3>Total Loss</h3></td>
                    <td><h3>:</h3></td>
                    <td><h3 class="h3_red"><label id="lbl_result" name="lbl_result"></label></h3></td>
                </tr>
                <tr>
                    <td><h3><label for="txt_current_weight">Today's Weight</label></h3></td>
                    <td><h3>:</h3></td>
                    <td><input type="text" id="txt_current_weight" name="txt_current_weight"></td>
                </tr>
            </table>
            <input type="button" name="clickbtn" value="Display Result" onclick="add_number()">
        </div>
           
        {js_code}
            
        <div class="float-child">
            <table>
                <tr>
                    <td><h3>Week 1</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week1_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week1_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 2</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week2_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week2_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 3</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week3_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week3_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 4</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week4_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week4_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 5</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week5_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week5_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 6</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week6_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week6_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 7</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week7_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week7_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 8</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week8_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week8_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 9</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week9_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week9_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 10</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week10_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week10_kgs}</h3></td>
                </tr>
            </table>
        </div>
        <div class="float-child">
            <table>
                <tr>
                    <td><h3>Week 11</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week11_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week11_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 12</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week12_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week12_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 13</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week13_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week13_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 14</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week14_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week14_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 15</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week15_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week15_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 16</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week16_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week16_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 17</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week17_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week17_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 18</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week18_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week18_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 19</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week19_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week19_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 20</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week20_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week20_kgs}</h3></td>
                </tr>
            </table>
        </div>
        <div class="float-child">
            <table>
                <tr>
                    <td><h3>Week 21</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week21_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week21_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 22</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week22_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week22_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 23</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week23_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week23_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 24</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week24_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week24_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 25</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week25_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week25_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 26</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week26_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week26_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 27</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week27_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week27_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 28</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week28_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week28_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 29</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week29_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week29_kgs}</h3></td>
                </tr>
                <tr>
                    <td><h3>Week 30</h3></td>
                    <td>:</td>
                    <td><h3 class="h3_black">{access.week30_loss}</h3></td>
                    <td><h3 class="h3_black"> - </h3></td>
                    <td><h3 class="h3_black">{access.week30_kgs}</h3></td>
                </tr>
            </table>
        </div>
        </div>
</body>
</html>
    """
    
    write_html( html_code, access.this_week_number )
    
###------------------------------------------------------------------------------
    
def write_html(html_code, week_number):
    filename = "WeightCalc_week" +str(week_number) +".html"
    
    html_file = open(filename, "w")
    html_file.write( html_code )
    html_file.close()
    
###------------------------------------------------------------------------------

access1 = Data()

# write_html("somecode", access1.this_week_number)

manipulate_jscode(access1)

# write_html("somecode", access1.this_week_number)
