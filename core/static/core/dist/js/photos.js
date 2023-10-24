document.addEventListener("DOMContentLoaded", function () {

    // Upload main_photo
    const upload_main_photo = document.getElementById('upload_main_photo')
    const delete_main_photo = document.getElementById('delete_main_photo')
    const main_photo_input = document.getElementById('main_photo')
    const img = document.getElementById('photo')

    upload_main_photo.addEventListener("click", function () {
        console.log('click upload button')
        main_photo_input.click();
    });

    main_photo_input.addEventListener("change", function () {
        const selectedFile = main_photo_input.files[0];

        if (selectedFile) {
            console.log('upload main photo:', selectedFile);
            img.setAttribute('src', URL.createObjectURL(selectedFile));
        }
    });

    delete_main_photo.addEventListener("click", function () {
        console.log('delete main photo')
    });
    // End Upload main_photo


    // Add new photo to gallery
    const addPhotoButton = document.getElementById('add-photo')
    const totalFormsInput = document.getElementById('id_form-TOTAL_FORMS');
    let totalForms = totalFormsInput ? parseInt(totalFormsInput.value) : 0;
    //console.log("totalFormsInput: ", totalFormsInput.value)

    // Get Target elements
    const ListTarget = document.getElementById('ingredient-form-list')

    addPhotoButton.addEventListener("click", function (event) {
        //console.log('click addButton')

        totalFormsInput.value = ++totalForms;
        //console.log("totalFormsInput: ", totalFormsInput.value)

        // Copy emptyForm
        const emptyForm = document.getElementById('empty-form').cloneNode(true)
        //console.log('emptyForm: ', emptyForm)
        emptyForm.setAttribute('class', 'ingredient-form col-3')
        emptyForm.setAttribute('id', `form-${totalFormsInput.value}`)

        const uploadInput = emptyForm.querySelector('input.custom-file-input')
        uploadInput.setAttribute('id', `input-${totalFormsInput.value}`)
        //console.log('uploadInput: ', uploadInput)

        const uploadButton = emptyForm.querySelector('button.file-upload')
        uploadButton.setAttribute('id', `btn-upload-${totalFormsInput.value}`)
        uploadButton.setAttribute('data-input', uploadInput.id)
        //console.log('uploadButton: ', uploadButton)

        const uploadImage = emptyForm.querySelector('img.card-img')
        uploadImage.setAttribute('id', `img-${totalFormsInput.value}`)
        //console.log('uploadImage: ', uploadImage)

        const regex = new RegExp('__prefix__', 'g')

        emptyForm.innerHTML = emptyForm.innerHTML.replace(regex, totalFormsInput.value)

        totalFormsInput.setAttribute('value', `${totalFormsInput.value}`)

        // Include copy emptyForm to Target element
        ListTarget.append(emptyForm)
    });

    ListTarget.addEventListener('click', function (event) {
            const target = event.target
            console.log('target: ', target)

            if (target.id.startsWith(`btn-upload`)) {

                const inputId = target.id.replace('btn-upload-', '');
                console.log('inputId: ', inputId)
                const uploadInput = document.getElementById(`input-${inputId}`);
                console.log('uploadInput: ', uploadInput)
                uploadInput.click()

                uploadInput.addEventListener("change", function () {

                    const selectedFile = uploadInput.files[0];

                    if (selectedFile) {
                        const formData = new FormData();
                        formData.append('photo', selectedFile);

                        console.log('Upload photo:', selectedFile);

                        const uploadImage = document.getElementById(`img-${inputId}`);
                        uploadImage.setAttribute('src', URL.createObjectURL(selectedFile));
                    }
                })
            }
        });
});
