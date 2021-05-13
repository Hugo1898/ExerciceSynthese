function getValue() {
      var t = document.getElementById("album-search").value;
      document.location.href = "/disks/albums/" + t;
   }