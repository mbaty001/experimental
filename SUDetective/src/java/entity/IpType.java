/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "IP_TYPE")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "IpType.findAll", query = "SELECT i FROM IpType i"),
    @NamedQuery(name = "IpType.findByIdIPTYPE", query = "SELECT i FROM IpType i WHERE i.idIPTYPE = :idIPTYPE"),
    @NamedQuery(name = "IpType.findByName", query = "SELECT i FROM IpType i WHERE i.name = :name")})
public class IpType implements Serializable {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idIP_TYPE")
    private Integer idIPTYPE;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "iPTYPEidIPTYPE")
    private List<Lab> labList;

    public IpType() {
    }

    public IpType(Integer idIPTYPE) {
        this.idIPTYPE = idIPTYPE;
    }

    public IpType(Integer idIPTYPE, String name) {
        this.idIPTYPE = idIPTYPE;
        this.name = name;
    }

    public Integer getIdIPTYPE() {
        return idIPTYPE;
    }

    public void setIdIPTYPE(Integer idIPTYPE) {
        this.idIPTYPE = idIPTYPE;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlTransient
    public List<Lab> getLabList() {
        return labList;
    }

    public void setLabList(List<Lab> labList) {
        this.labList = labList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idIPTYPE != null ? idIPTYPE.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof IpType)) {
            return false;
        }
        IpType other = (IpType) object;
        if ((this.idIPTYPE == null && other.idIPTYPE != null) || (this.idIPTYPE != null && !this.idIPTYPE.equals(other.idIPTYPE))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.IpType[ idIPTYPE=" + idIPTYPE + " ]";
    }
    
}
