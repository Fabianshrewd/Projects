using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WASD_Movement : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //Declare variables
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        float speed = 5.0f;

        //Add the changes to the object
        if(Input.GetKey(KeyCode.W)) {
             transform.position += transform.forward * Time.deltaTime * speed;
        }
    }
}
