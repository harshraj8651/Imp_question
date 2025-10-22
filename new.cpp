#include <iostream>
using namespace std;

// Node structure
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int value) {
        data = value;
        left = right = nullptr;
    }
};

// Insert function
Node* insert(Node* root, int value) {
    if (root == nullptr) { // Empty spot found
        return new Node(value);
    }
    if (value < root->data) {
        root->left = insert(root->left, value);
    } 
    else if (value > root->data) {
        root->right = insert(root->right, value);
    }
    return root;
}

// Search function
bool search(Node* root, int value) {
    if (root == nullptr) return false;
    if (root->data == value) return true;
    if (value < root->data) return search(root->left, value);
    else return search(root->right, value);
}

// Inorder traversal (sorted output)
void inorder(Node* root) {
    if (root != nullptr) {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

int main() {
    Node* root = nullptr;
    
    // Insert elements
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 60);
    root = insert(root, 80);
    
    // Print sorted elements
    cout << "Inorder Traversal: ";
    inorder(root);
    cout << endl;
    
    // Search
    int key = 60;
    if (search(root, key))
        cout << key << " found in the BST\n";
    else
        cout << key << " not found in the BST\n";
    
    return 0;
}
