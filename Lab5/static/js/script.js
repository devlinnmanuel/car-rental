document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('add-student');
    const form = document.getElementById('myForm');
    
    // Toggle form
    button.addEventListener('click', function() {
        const update_form = document.getElementById('myFormUpdate');
        update_form.style.display = update_form.style.display === 'block' ? 'none' : 'none';

        form.style.display = form.style.display === 'none' ? 'block' : 'none';
        document.getElementById('nim').value = "";
        document.getElementById('nama').value = "";
        document.getElementById('tgl-lahir').value = "";
    });

    // memunculkan form update dengan data yang diambil
    document.querySelectorAll('.open-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            let studentData = {
                id: this.dataset.id,
                nim: this.dataset.nim,
                nama: this.dataset.nama,
                tgl_lahir: this.dataset.tgl_lahir
            };
        
            document.getElementById('nimUpdate').value = studentData.nim;
            document.getElementById('namaUpdate').value = studentData.nama;
            document.getElementById('tgl-lahirUpdate').value = studentData.tgl_lahir;
    
            document.getElementById('myForm').style.display = 'none';
            document.getElementById('myFormUpdate').style.display = 'block';

            // untuk update student:
            document.getElementById('update').addEventListener('click', function () {
                const id = studentData.id;
                nim = document.getElementById('nimUpdate').value;
                nama = document.getElementById('namaUpdate').value;
                tgl_lahir = document.getElementById('tgl-lahirUpdate').value;
                window.location.href = `/update-student/${id}/${nim}/${nama}/${tgl_lahir}`;
            });

            // untuk delete student:
            document.getElementById('delete').addEventListener('click', function () {
                const id = studentData.id;
                window.location.href = `/delete-student/${id}`;
            });
        });
    });
});