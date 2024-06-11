document.getElementById('add-cat-form').addEventListener('submit', function(event) {
    // Prevent the form's default behavior
    event.preventDefault();

    // Get the values from the form fields
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let clinic = document.getElementById('clinic').value;
    let healthStatus = document.getElementById('healthStatus').value;

    // Check if we're editing an existing cat or adding a new one
    if (this.editRow) {
        // Update the details of the cat being edited
        this.editRow.children[0].textContent = name;
        this.editRow.children[1].textContent = age;
        this.editRow.children[2].textContent = clinic;
        this.editRow.children[3].textContent = healthStatus;

        // Clear the reference to the row being edited
        this.editRow = null;
    } else {
        // Add the new cat to the table
        addCatToTable(name, age, clinic, healthStatus);
    }

    // Clear the form fields
    this.reset();
});

function addCatToTable(name, age, clinic, healthStatus) {
    // Create a new row and cells for the table
    let row = document.createElement('tr');
    let nameCell = document.createElement('td');
    let ageCell = document.createElement('td');
    let clinicCell = document.createElement('td');
    let healthStatusCell = document.createElement('td');
    let editCell = document.createElement('td');
    let removeCell = document.createElement('td');

    // Create the Edit button
    let editButton = document.createElement('button');
    editButton.textContent = 'Editar';
    editButton.className = 'edit-btn';
    editButton.addEventListener('click', function() {
        // Populate the form with the cat's current details
        document.getElementById('name').value = nameCell.textContent;
        document.getElementById('age').value = ageCell.textContent;
        document.getElementById('clinic').value = clinicCell.textContent;
        document.getElementById('healthStatus').value = healthStatusCell.textContent;

        // Save a reference to the row being edited
        document.getElementById('add-cat-form').editRow = row;
    });

    // Create the Remove button
    let removeButton = document.createElement('button');
    removeButton.textContent = 'Remover';
    removeButton.className = 'remove-btn';
    removeButton.addEventListener('click', function() {
        // Remove the row from the table
        row.remove();
    });

    // Add the buttons to the cells
    editCell.appendChild(editButton);
    removeCell.appendChild(removeButton);

    // Set the text of the cells
    nameCell.textContent = name;
    ageCell.textContent = age;
    clinicCell.textContent = clinic;
    healthStatusCell.textContent = healthStatus;

    // Add the cells to the row
    row.appendChild(nameCell);
    row.appendChild(ageCell);
    row.appendChild(clinicCell);
    row.appendChild(healthStatusCell);
    row.appendChild(editCell);
    row.appendChild(removeCell);

    // Add the row to the table
    document.getElementById('cats-table').appendChild(row);
}