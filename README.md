# plastic-material-classification-hyperspectral-data

### Data Pre-Processor

This repository contains the preprocessing pipeline for converting raw spectral data into a format suitable for machine learning models. The pipeline performs the following tasks:

- Converts `.xlsx` datasets to `.csv`
- Cleans the dataset:
  - Performs data splice correction
  - Computes the average of pseudo-replicates for the same sample
  - Filters out calibration and irrelevant samples
- Creates a labeled dataset for supervised learning
- Splits the dataset into training and testing sets (stratified)
- Prepares data for K-fold cross-validation if needed

---

### Requirements

The following dependencies are required:

- Python >= 3.10
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)
- [matplotlib](https://matplotlib.org/) (optional for plotting)

Install them via pip:

```bash
pip install pandas numpy openpyxl scikit-learn matplotlib
````

---

### Dataset

1. Create the dataset folder if it doesn't exist:

```bash
mkdir -p dataset
```

2. Place your raw dataset Excel file in the `dataset` folder as:

```
dataset/dataset.xlsx
```

3. The preprocessing script expects the Excel file to have at least:

   * **Sheet 1:** Metadata (sample info)
   * **Sheet 2:** Raw spectral data with wavelengths as the index

---

### Data Processing Steps

1. **Convert Excel to CSV**
2. **Load CSV files**
3. **Verify data range [0,1]**
4. **Average pseudo-replicates and remove calibration samples**
5. **Select polymers for classification** (PET, PP, PE, PS)
6. **Create labeled dataset**
7. **Split into training and test sets**
8. **Export final dataset** (`xtrain.csv`, `xtest.csv`, `ytrain.csv`, `ytest.csv`)

The notebook `data_preprocessor.ipynb` contains all the code for these steps.

---

### Notes

* Ensure `dataset.xlsx` is correctly formatted and placed in the `dataset` folder.
* Calibration samples are automatically filtered out during preprocessing.
* Final CSV files are ready to be used for machine learning pipelines.

---

### References

* [pandas Documentation](https://pandas.pydata.org/)
* [scikit-learn Documentation](https://scikit-learn.org/)

### Authors:  
- Fábio D. Pacheco, up202502538  
- Maximino Samarychev, up202107590  
- Filipe Ramos, up202208996  
