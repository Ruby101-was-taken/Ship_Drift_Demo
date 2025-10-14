using ShipDrift.Behaviour.Player;
using UnityEngine;

public class PlayerContext : MonoBehaviour
{
    [SerializeField]
    public static PlayerBehaviour playerBehaviour_;

    [SerializeField]
    private PlayerBehaviour player;

    private void Awake() {
        playerBehaviour_ = player;
    }
}
