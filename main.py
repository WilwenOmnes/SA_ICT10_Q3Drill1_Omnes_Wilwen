        #Comment: Scores were renamed to different variables like math and science. 
        #Scores remain done in the same way as the previous average finder, score 3 was just added.
from pyscript import document

def compute_average(event):
    math = document.getElementById("score1").value.strip()
    science = document.getElementById("score2").value.strip()
    english = document.getElementById("score3").value.strip()

    if not math or not science or not english:
        document.getElementById("average").innerText = "—"
        document.getElementById("result").innerText = "Fill everything out man"
        return

    try:
        math = float(math)
        science = float(science)
        english = float(english)

        if (
            math < 60 or math > 100 or
            science < 60 or science > 100 or
            english < 60 or english > 100
        ):
            document.getElementById("average").innerText = "—"
            document.getElementById("result").innerText = "60 - 100 only. Dont lie to me"
            return

        average = (math + science + english) / 3

        #Conditionals were added, such as if elif and else statements.
        if average == 100:
            result = "No way..."
        elif average > 90 and average <99.99:
            result = "Pretty good"
        elif average > 85 and average <89.99:
            result = "Pass"
        elif average > 75 and average < 84.99:
            result = "Passed but try harder"
        else:
            result = "Trying to fail on purpose?"

        document.getElementById("average").innerText = str(round(average, 2))
        document.getElementById("result").innerText = result

    except ValueError:
        document.getElementById("average").innerText = "—"
        document.getElementById("result").innerText = "Use numbers smh"