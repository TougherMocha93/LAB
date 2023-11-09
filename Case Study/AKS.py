import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert('L')  
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
    mean = np.mean(image, axis=0)
    normalized_image = image - mean
    cov_matrix = np.cov(normalized_image, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    idx = eigenvalues.argsort()[::-1]
    eigenvectors = eigenvectors[:, idx]  
    components = eigenvectors[:, :n_components]
    compressed_image = np.dot(components.T, normalized_image.T).T 
    reconstructed_image = np.dot(components, compressed_image.T).T + mean

    return reconstructed_image

if __name__ == "__main__":
    image_path = 'original_image.jpg'
    original_image = load_image(image_path)


    num_components = 50  


    compressed_image = image_compression_pca(original_image, num_components)


    plot_comparison(original_image, compressed_image)