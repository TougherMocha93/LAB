import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert('L')  # Convert the image to grayscale
    img = np.array(img)
    return img

def plot_comparison(original, compressed):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(original, cmap='gray')
    ax[0].set_title('Original Image')
    ax[0].axis('off')

    ax[1].imshow(compressed, cmap='gray')
    ax[1].set_title('Compressed Image')
    ax[1].axis('off')

    plt.show()

def image_compression_pca(image, n_components):
    # Mean normalization
    mean = np.mean(image, axis=0)
    normalized_image = image - mean

    # Calculate the covariance matrix
    cov_matrix = np.cov(normalized_image, rowvar=False)

    # Compute eigenvectors and eigenvalues
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Sort eigenvalues and corresponding eigenvectors
    idx = eigenvalues.argsort()[::-1]
    eigenvectors = eigenvectors[:, idx]
    
    # Choose the top n_components eigenvectors
    components = eigenvectors[:, :n_components]

    # Project the normalized image onto the selected components
    compressed_image = np.dot(components.T, normalized_image.T).T

    # Inverse transformation to reconstruct the image
    reconstructed_image = np.dot(components, compressed_image.T).T + mean

    return reconstructed_image

# Load the image
image_path = 'original_image.jpg'
original_image = load_image(image_path)

# Set the number of principal components for compression
num_components = 50  # Adjust this to change the level of compression

# Compress the image using PCA
compressed_image = image_compression_pca(original_image, num_components)

# Plot the original and compressed images
plot_comparison(original_image, compressed_image)
