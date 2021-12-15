using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Lock_Mouse : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        //Lock the cursor and make it invisibl
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
