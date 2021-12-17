﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Look_Right_and_Left : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    //Declare some things for the rotation
    float rotationX = 0f;
    float rotationY = 0f;
    public float sensitivity = 15f;

    // Update is called once per frame
    void Update()
    {
        //Calculate the moved sensivity
        rotationY += Input.GetAxis("Mouse X") * sensitivity;
        transform.localEulerAngles = new Vector3(rotationX, rotationY, 0);
    }
}