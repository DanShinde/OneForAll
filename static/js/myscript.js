var groups = {{ user.groups.all }};
var timesheetNav = document.getElementById("timesheet-nav");

for (var i = 0; i < groups.length; i++) {
    if (groups[i].name === "timesheet") {
        timesheetNav.style.display = "block";
        break;
    }
}