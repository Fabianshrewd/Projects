using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WASD_Movement : MonoBehaviour
{
    public float size = 0.1f;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        GameObject player = GameObject.Find("Player");
        size += 0.1f;
        player.transform.position = new Vector3(size, 0, 0);
    }
}
