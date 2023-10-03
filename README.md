# Signature Recognition

Signature recognition is a powerful behavioral biometric method for verifying and authenticating individuals based on their unique signatures. This README provides an overview of signature recognition, its two primary modes of operation, and the prerequisites for running this project.

## Modes of Operation

Signature recognition can be operated in two distinct modes:

### Static (Offline)

In the static mode, users create their signatures on paper, which are then digitized using optical scanners or cameras. The biometric system analyzes the shape and features of these digitized signatures to perform recognition. This mode is often referred to as "offline" recognition.

### Dynamic (Online)

In the dynamic mode, users create their signatures using a digitizing tablet, stylus-operated PDAs, or even smartphones or tablets with capacitive screens. This mode allows for real-time acquisition of the signature. Dynamic recognition is also known as "online" recognition.

Dynamic recognition captures additional information about the signature, including various dynamic features:

- **Pressure**: The force applied while signing.
- **Speed**: The rate at which the signature is drawn.
- **Acceleration**: Changes in speed during the signing process.
- **Pen Tilt**: The angle at which the pen or stylus is held.

## Prerequisites

Before you can run this project, ensure that you have the following Python modules installed:

```bash
pip install keras
pip install numpy
pip install pandas
pip install sklearn
pip install os
pip install matplotlib
